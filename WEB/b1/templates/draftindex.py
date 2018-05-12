

    # <!-- jinja2 --> hien 1 post, chua dung vong for
<!--  <h5>{{ post['title'] }}</h5> bang voi cai o duoi -->
<h5>{{ post.title }}</h5>
<p>
  {{post.content}}
</p>

<i>By: {{post.author}}</i>
