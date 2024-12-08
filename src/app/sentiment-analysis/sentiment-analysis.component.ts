import { Component } from '@angular/core';

@Component({
  selector: 'app-sentiment-analysis',
  standalone: true,
  templateUrl: './sentiment-analysis.component.html',
  styleUrl: './sentiment-analysis.component.css'
})
export class SentimentAnalysisComponent {
  text: string = ' ';
}
