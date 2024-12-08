import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-news-item',
  standalone: true,
  templateUrl: './news-item.component.html',
  styleUrl: './news-item.component.css'
})
export class NewsItemComponent {
  @Input() title: string = "";
  @Input() description: string = '';
  @Input() url: string = '';
  @Input() imageUrl: string = '';
  @Input() publishedAt: string = '';
}
