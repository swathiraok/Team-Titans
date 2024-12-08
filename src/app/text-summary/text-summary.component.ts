import { Component } from '@angular/core';

@Component({
  selector: 'app-text-summary',
  standalone: true,
  templateUrl: './text-summary.component.html',
  styleUrl: './text-summary.component.css'
})
export class TextSummaryComponent {
  summaryText: string = " "; 
}
