import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class NewsService {
  private apiUrl = 'http://127.0.0.1:5000/fetch-news';

  constructor(private http: HttpClient) {}

  fetchNews(interest: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}?interest=${interest}`);
  }
}
