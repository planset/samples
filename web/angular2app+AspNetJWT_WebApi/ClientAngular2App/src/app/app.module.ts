import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule }    from '@angular/http';

import {routing} from './app.routing';
import { HeroService }   from './hero.service';
import { AuthGuard}   from './_guards/auth.guard';
import { AuthenticationService }   from './_services/authentication.service';
import { AppComponent }  from './app.component';
import {LoginComponent} from'./login/login.component';
import {HomeComponent} from'./home.component';

@NgModule({
  imports:      [ 
    BrowserModule,
    FormsModule,
    HttpModule,
    routing
     ],
  declarations: [ 
    AppComponent,
    LoginComponent,
    HomeComponent
    ],
  providers: [
    HeroService,
    AuthGuard,
    AuthenticationService,
    ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
