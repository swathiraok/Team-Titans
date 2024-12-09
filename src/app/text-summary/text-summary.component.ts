import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-text-summary',
  standalone: true,
  templateUrl: './text-summary.component.html',
  styleUrl: './text-summary.component.css',
  imports: [FormsModule, CommonModule]
})
export class TextSummaryComponent {
  summaryText: string = " "; 

  textSumamry = [
    {
      articleId: "12345",
      summary: "The stock market reached new record highs, driven by strong economic growth and investor optimism."
    },
    {
      articleId: "12346",
      summary: "Technology stocks experienced a decline due to increasing regulatory scrutiny."
    },
    {
      articleId: "234566",
      summary: "The stock market reached new record highs, driven by strong economic growth and investor optimism."
    },
    {
      articleId: "567888",
      summary: "Technology stocks experienced a decline due to increasing regulatory scrutiny."
    }
  ];

  textSummaryData = [
    {
      originalText: "The quick brown fox jumps over the lazy dog.",
      summary: "A fox jumps over a dog."
    },
    {
      originalText: "Angular is a platform for building mobile and desktop web applications.",
      summary: "Angular is a platform for web applications."
    }
  ];
}
