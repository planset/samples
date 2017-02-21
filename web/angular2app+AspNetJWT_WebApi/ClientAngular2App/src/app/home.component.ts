import { Component } from '@angular/core';

import { Hero } from './hero';
import { HeroService} from './hero.service';

@Component({
  selector: 'home',
  template:  `
  <h2>{{hero.name}} details!</h2>
  <div><label>id: </label>{{hero.id}}</div>
  <div>
  <label>name: </label>
  <input [(ngModel)]="hero.name" plcaeholder="name">
  </div>
  `
})
export class HomeComponent  { 
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

