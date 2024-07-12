# Virtual Art Gallery DRF-API Manual Testing

## Methodology

By going through the user stories one by one, we should be able to assure that all functions are working as expected.
Therefor, a series of tests have been performed below.

Write review on posts:

**Acceptance Criteria
- Toggle review button
- Type content in text field
- Add a rating between 1 & 5
- Publish review button

<p>
    <img src="documentation/testing/review/review_content_400.png">
</p>

* Edit Review
***Acceptance Criteria

 - Toggle edit review button
 - Edit review in text field
 - Toggle save review button
 - Reviews count increases by 1
 - Rating will increase or decrease

<p>
    <img src="documentation/testing/review/review_content_rating_201.png">
</p>

- If content field is not filled in, a 400 alert will return. 

<p>
    <img src="documentation/testing/review/review_content_400.png">
</p>

- If an integer between 1 & 5 is not assigned, a 400 error will throw.

<p>
    <img src="documentation/testing/review/revirew_rating_400.png">
</p>

- Title and tags are not mandatory, just content and rating.

<p>
    <img src="documentation/testing/review/review_edit_content_rating_200.png">
</p>

- A review with all fields filled out

<p>
    <img src="documentation/testing/review/post_review_all_201.png">
</p>


* Delete Review
***Acceptance Criteria

- Toggle delete review button
- Accept query to remove review
- Review will be removed

<p>
    <img src="documentation/testing/review/review_delete_204.png">
</p>

* As a user I can create my own unique profile so that I can get access to all the features on the site

***Acceptance Criteria

 Create unique username
 Create unique password
 Login and logout function

<p>
    <img src="documentation/testing/authorization/register_201.png">
</p>
 

<p>
    <img src="documentation/testing/authorization/login_405.png">
</p>

- Returned when a user is logged out:

<p>
    <img src="documentation/testing/authorization/logout_200.png">
</p>

- When a user is requesting a password reset:
 There's no reset email sent, however.
<p>
    <img src="documentation/testing/authorization/password_reset_200.png">
</p>

- If a user wishes to change password, the database returns a 200 message:

<p>
    <img src="documentation/testing/authorization/password_change_200.png">
</p>

- If a user types types an invalid password in one of fields, the database returns a 400 error:

<p>
    <img src="documentation/testing/authorization/password_change_400.png">
</p>

- If a field is empty, the database will return a 400 error with an appropriate message saying that he field cannot be blank:

<p>
    <img src="documentation/testing/authorization/password_reset_400.png">
</p>

- A new registered user can register with a username and password. Email and full name is not necessary.



- A new user cannot register, without entering a username or a valid password.

<p>
    <img src="documentation/testing/authorization/register_405.png">
</p>

- If a user enters a password that is too common ot too short, the database will return a 400 error message, and a hint that 
the password is too common or too short.

<p>
    <img src="documentation/testing/authorization/register_too_common_400.png">
</p>

- When a user chooses to follow another user, the field named "followed" will increase by one integer and the database will 
answer with a 200 created. 

<p>
    <img src="documentation/testing/followers/follower_create_201.png">
</p>

- When a user stops following another user, the database will respond with 204 no content and.

<p>
    <img src="documentation/testing/followers/follower_delete_204.png">
</p>

- Likes

<p>
    <img src="documentation/testing/likes/likes_200.png">
</p>

- When a user likes another users post, the json message returns the id of the post and an appropriate message 201 created.

<p>
    <img src="documentation/testing/likes/likes_201.png">
</p>

- If a user unlikes a post the like id will be deleted from the database which wil return the json message and 204 no content.

<p>
    <img src="documentation/testing/likes/likes_204.png">
</p>

- When a user uploads a new posts, all the fields that are filled out will be visible in the json message and a 201 created message will be returned. The profile id of the user will also e displayed.

<p>
    <img src="documentation/testing/posts/post_.png">
</p>

- Note that not all fields are mandatory:

<p>
    <img src="documentation/testing/posts/post_create_all.png">
</p>

- When a post is deleted, the appropriate 204 message will be returned:

<p>
    <img src="documentation/testing/posts/post_delete_204.png">
</p>

- If a user edits and updates a post, the database will return a 200 OK message.

<p>
    <img src="documentation/testing/posts/post_edit_all_200.png">
</p>

- The only two mandadatory fields when creating a new post, are title and the image field. The database will return a 201 created.

<p>
    <img src="documentation/testing/posts/post_title_201.png">
</p>

* As a user I can change my username and password so that I can keep my personal details safe

***Acceptance Criteria

 Change username
 Change password
 Save changes

- If a user wishes to update the profile, the database will return the new values with a 200 message:

<p>
    <img src="documentation/testing/profiles/profile_update_200.png">
</p>

- Profile list:

<p>
    <img src="documentation/testing/profiles/profile_list_200.png">
</p>

- If the user is looking for a profile that doesn't exits, the database will respond with a 400 message.
This is also the case if a user chooses to have the profile deleted:

<p>
    <img src="documentation/testing/profiles/profile_400.png">
</p>


| Test Case | Description | Result | Comments |
|-----------|-------------|--------|----------|