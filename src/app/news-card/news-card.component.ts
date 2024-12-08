import { Component, Input } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button'; 

@Component({
  selector: 'app-news-card',
  standalone: true,  // Make it standalone
  templateUrl: './news-card.component.html',
  styleUrls: ['./news-card.component.scss'],
  imports: [MatCardModule, MatButtonModule]
})
export class NewsCardComponent {
  @Input() news: any;
  // newsTitle = "IND vs AUS 2023: Cameron Green";
  // newsSource = "The Cricket Times";
  // newsTime = "9/24/2023, 8:15:09 PM";
  // newsDescription = "Australia all-rounder Cameron Green conceded 103 runs in his quota of ten overs against India...";
}
