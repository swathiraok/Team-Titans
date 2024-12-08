import { Component } from '@angular/core';
import { HeaderComponent } from "../header/header.component";

@Component({
  selector: 'app-team-ai-titans',
  standalone: true,
  templateUrl: './team-ai-titans.component.html',
  styleUrl: './team-ai-titans.component.css',
  imports: [HeaderComponent]
})

export class TeamAiTitansComponent {
  constructor() { }
}
