import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamAiTitansComponent } from './team-ai-titans.component';

describe('TeamAiTitansComponent', () => {
  let component: TeamAiTitansComponent;
  let fixture: ComponentFixture<TeamAiTitansComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TeamAiTitansComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TeamAiTitansComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
