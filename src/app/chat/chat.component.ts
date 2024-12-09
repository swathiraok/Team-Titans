import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NewsService } from '../news.service';
import { CommonModule } from '@angular/common';
import { NewsItemComponent } from '../news-item/news-item.component';

@Component({
  selector: 'app-chat',
  standalone: true,
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss'],
  imports: [NewsItemComponent, FormsModule, HttpClientModule, CommonModule],
  providers: [NewsService]
})
export class ChatComponent {
  userInput: string = '';
  aiResponse: any[] = [];

  constructor(private newsService: NewsService) { }

  handleEnter(event: KeyboardEvent) {
    event.preventDefault();
    this.resetTextArea();
    this.getAiResponse();
  }


  getAiResponse() {
    this.newsService.fetchNews(this.userInput).subscribe(
      (response) => {
        this.aiResponse = response.articles;
      },
      (error) => {
        console.error('Error fetching data from API', error);
      }
    );
  }

  resetTextArea() {
    this.userInput = '';
  }
}
