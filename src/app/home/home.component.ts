import { Component } from '@angular/core';
import { SentimentAnalysisComponent } from "../sentiment-analysis/sentiment-analysis.component";
import { TextSummaryComponent } from "../text-summary/text-summary.component";
import { ChatComponent } from "../chat/chat.component";

@Component({
  selector: 'app-home',
  standalone: true,
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
  imports: [ChatComponent, TextSummaryComponent, SentimentAnalysisComponent]
})
export class HomeComponent {

}
