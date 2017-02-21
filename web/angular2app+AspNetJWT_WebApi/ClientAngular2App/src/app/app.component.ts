import { Component } from '@angular/core';

import { Hero } from './hero';
import { HeroService} from './hero.service';

@Component({
  selector: 'my-app',
  template:  `<h1>{{title}}</h1>
  <!-- main app container -->
  <div class="jumbotron">
      <div class="container">
          <div class="col-sm-8 col-sm-offset-2">
              <router-outlet></router-outlet>
          </div>
      </div>
  </div>
  `
})
export class AppComponent  { 
  title = 'Tour of Heroess';
  hero: Hero = {
    id: 1,
    name: 'windstorm'
  };

  constructor(private heroService: HeroService){
    heroService.getHeroes().subscribe((heros) => {
      this.hero = heros[0];
    });

  }
}
