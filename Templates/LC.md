<%* let title = tp.file.title
  if (title.startsWith("Untitled")) {
    title = await tp.system.prompt("Title");
    await tp.file.rename(title);
  } 
-%>
<%*
  let result = title.replace(/-/g, ' ')
  result = result.charAt(0).toUpperCase() + result.slice(1);
  tR += "---"
%>
title:  <%* tR += "\"" + result + "\"" %>
tags:
<% tp.file.cursor(1) %>
created: <% tp.date.now("YYYY-MM-DD") %>
---

>[!summary]+ Contents
>```toc
>style: number
>min_depth:1
>max_depth:6
>```


# Description


# Intuition

>[!danger]+ Intuition

# Implementation


>[!example]+ 


# Related
