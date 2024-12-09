import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { TeamAiTitansComponent } from './team-ai-titans/team-ai-titans.component';



const routes: Routes = [
    { path: 'team', component: TeamAiTitansComponent }, // Team route
    // { path: '', redirectTo: '/home', pathMatch: 'full' }, 
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
  })

export class AppRoutingModule { }
