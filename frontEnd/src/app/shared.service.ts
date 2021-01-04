import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIUrl = "http://127.0.0.1:8000";
  constructor(private http:HttpClient) { }

  getCatList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/categories/');
  }
  addCategories(val:any){
    return this.http.post(this.APIUrl + '/categories/', val);
  }
  updateCategories(val:any){
    return this.http.put(this.APIUrl + '/categories/', val);
  }
  deleteCategories(val:any){
    return this.http.delete(this.APIUrl + '/categories/', val);
  }


  getArtList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/article/');
  }
  addArticles(val:any){
    return this.http.post(this.APIUrl + '/article/', val);
  }
  updateArticles(val:any){
    return this.http.put(this.APIUrl + '/article/', val);
  }
  deleteArticles(val:any){
    return this.http.delete(this.APIUrl + '/article/', val);
  }
}
