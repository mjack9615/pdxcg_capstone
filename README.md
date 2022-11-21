
# FinalBoss CRT

Possessing a large video game collection is fun but also potentially challenging and occasionally frustrating. FinalBoss CRT (Collection & Research Tool) is here to provide the game collector with transparency and a path toward better collection utilization.


## Features

When a collection grows to a massive size it can become very difficult to keep track of specific information such as how many copies of a title are owned or which platform a particular game belongs to. Being able to prioritize which games should be played next is also important so that available gaming time isn't wasted and highly rated titles aren't being missed. Additionally, staying on top of newly released games is vital to keeping a collection current and complete. In order to facilitate the necessary level of organization, FinalBoss allows the user to:

- Create a personal database of titles with records stored by name, platform and review score (if available)
- Interact with the database through creation, modification or deletion of individual records
- Filter the database by keyword, platform and review score
- Display a sorted list of the highest rated titles in the collection
- Search for titles, display screenshots or watch trailers via the RAWG Video Games Database


## Techology

FinalBoss is coded in the Django Python Framework, Vue.js, HTML and CSS.

Access to the features of FinalBoss is only provided to authenticated users. Account creation consists of the selection of a username and password.

The user's collection is stored in an SQLite database and modified directly by Django when creating, updating or deleting records.

The data model for the database:

    title = CharField
    platform = CharField
    score = IntegerField




## Schedule

11.21.22--11.25.22 Site design, initial setup of Django project, begin coding app logic

11.28.22--12.2.22 Finalize app logic, begin styling  

12.5.22--12.9.22 Testing, debugging, final styling


