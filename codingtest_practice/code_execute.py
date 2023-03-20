<form action="{% url 'articles:create' %}" method="POST">
  __(a)__
  <label for="__(b)__">Title: </label>
  <input type="text" name="title" id="title"><br>
  <label for="__(c)__">Content: </label>
  <textarea name="content" cols="30" rows="5" id="content"></textarea><br>
  <input type="submit">
</form>
