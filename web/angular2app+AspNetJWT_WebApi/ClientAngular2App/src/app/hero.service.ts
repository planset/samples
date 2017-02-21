import { Injectable }    from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Observable';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import { AuthenticationService } from './_services/authentication.service';

import { Hero } from './hero';

export class BaseService {
    constructor(
        protected router: Router,
        protected http: Http,
        protected authenticationService: AuthenticationService
        ) { }

    get(url:string, options:RequestOptions = null){
        let _headers = new Headers({ 'Authorization': 'Bearer ' + this.authenticationService.token });
        let _options = new RequestOptions({ headers: _headers });
        options = options.merge(_options);
        return this.http.get(url, options)
            .map(res => res.json() as Hero[])
            .catch(this.__handleError.bind(this));
    }

    private __handleError(error: any): Observable<any> {
        console.log('BaseService handleError');
        if(error.status == 401){
            this.router.navigate(['/login']);
        }
        return Observable.throw(error.json().error || 'Server error');
    }
}

@Injectable()
export class HeroService extends BaseService{

    private heroesUrl = '//localhost:51343/api/RequiredAuthValues';  // URL to web api

    constructor(
        router: Router,
        http: Http,
        authenticationService: AuthenticationService
        ) 
    {
        super(router, http, authenticationService);
    }

    getHeroes(): Observable<Hero[]> {
        let headers = new Headers({ 'Authorization': 'Bearer ' + this.authenticationService.token });
        let options = new RequestOptions({ headers: headers });
        
        return this.get(this.heroesUrl, options)
            .catch(this.handleError.bind(this));
    }

    private handleError(error: any): Observable<any> {
        console.log('HeroService handleError');
        return Observable.throw(error.json().error || 'Server error');
    }
}