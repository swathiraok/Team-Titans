import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { TeamAiTitansComponent } from './team-ai-titans/team-ai-titans.component';
import { HomeComponent } from './home/home.component';
import { PresentationComponent } from './presentation/presentation.component';



const routes: Routes = [
    { path: 'team', component: TeamAiTitansComponent },
    { path: 'presentation', component: PresentationComponent },
    { path: '', redirectTo: '/home', pathMatch: 'full' }, 
    { path: 'home', component: HomeComponent}
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
  })

export class AppRoutingModule { }
