import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-sentiment-analysis',
  standalone: true,
  templateUrl: './sentiment-analysis.component.html',
  styleUrl: './sentiment-analysis.component.css',
  imports: [FormsModule, CommonModule]
})
export class SentimentAnalysisComponent {
  text: string = ' ';


  
  sentimentData = [{
    articleId: "12345",
    headline: "Stock Market Hits Record Highs Amid Economic Growth",
    publishedDate: "2024-12-09",
    source: "MarketWatch",
    sentiment: "positive",
    confidenceScore: 0.92
  },
  {
    articleId: "12346",
    headline: "Tech Stocks Decline Following Regulatory Concerns",
    publishedDate: "2024-12-08",
    source: "Reuters",
    sentiment: "negative",
    confidenceScore: 0.85
  },
  {
    articleId: "12345",
    headline: "Stock Market Hits Record Highs Amid Economic Growth",
    publishedDate: "2024-12-09",
    source: "MarketWatch",
    sentiment: "neutral",
    confidenceScore: 0
  },
  {
    articleId: "12346",
    headline: "Tech Stocks Decline Following Regulatory Concerns",
    publishedDate: "2024-12-08",
    source: "Reuters",
    sentiment: "negative",
    confidenceScore: -2
  }
];
}
