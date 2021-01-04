import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CategoriesComponent } from './categories/categories.component';
import { ShowCatComponent } from './categories/show-cat/show-cat.component';
import { AddEditCatComponent } from './categories/add-edit-cat/add-edit-cat.component';
import { ArticlesComponent } from './articles/articles.component';
import { ShowArtComponent } from './articles/show-art/show-art.component';
import { AddEditArtComponent } from './articles/add-edit-art/add-edit-art.component';

import { SharedService } from './shared.service';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms'

@NgModule({
  declarations: [
    AppComponent,
    CategoriesComponent,
    ShowCatComponent,
    AddEditCatComponent,
    ArticlesComponent,
    ShowArtComponent,
    AddEditArtComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
