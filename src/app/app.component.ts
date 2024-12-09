import { Component } from '@angular/core';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from './header/header.component';
import { LeftSidebarComponent } from './left-sidebar/left-sidebar.component';
import { SentimentAnalysisComponent } from "./sentiment-analysis/sentiment-analysis.component";
import { TextSummaryComponent } from "./text-summary/text-summary.component";
import { ChatComponent } from "./chat/chat.component";
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  imports: [RouterOutlet, HeaderComponent, LeftSidebarComponent, SentimentAnalysisComponent, TextSummaryComponent, ChatComponent]
})
export class AppComponent {
  title = 'AI Agent UI';
}