import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';  // Import the standalone AppComponent
import { provideRouter } from '@angular/router';
import { AppRoutingModule } from './app/app-routing.module';
import { importProvidersFrom } from '@angular/core';

bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(AppRoutingModule) // Use AppRoutingModule for routing
  ]
}).catch(err => console.error(err));
