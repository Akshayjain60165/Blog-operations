# Blog-operations
This is purely backend part for different curd operations on Blog in django 


I have used Sql here(connected postgresql to django) because SQL databases provide great benefits for transactional data whose structure doesn’t change frequently (or at all) and where data integrity is paramount. It’s also best for fast analytical queries.

I have made 2 tables in which one is for content about blog(name is blog and can be seen in models.py of content folder) and the other one is for comments
blog have 3 attributes(blog_id,place,title)in which blog_id is intergerfield place is charfield and title is textfield and blog_id is primary key

In my homepage i have made 7 urls of addblog,deleteblog,seeallblog,seeblogbyid,updateblog,postcomment,seecomment(all can be seen in views.py of contents)

And for further classification my emial id is 2018ceb1002@iitrpr.ac.in
