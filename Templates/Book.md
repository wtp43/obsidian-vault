---
dg-publish: true
---
<%* let title = tp.file.title
  if (title.startsWith("Untitled")) {
    title = await tp.system.prompt("Title");
    await tp.file.rename(title);
  } 
-%>
<%* let author = tp.file.title
  if (author.startsWith("Untitled")) {
    author = await tp.system.prompt("Author");
  } 
-%>
<%*
  let result = title.replace(/-/g, ' ')
  result = result.charAt(0).toUpperCase() + result.slice(1);
  tR += "---"
%>
title:  <%* tR += "\"" + result + "\"" %>
author:  <%* tR += "\"" + author + "\"" %>
tags:
- book
- <% tp.file.cursor(1) %>
started reading: <% tp.date.now("YYYY-MM-DD") %>
finished reading: 

---

# Summary