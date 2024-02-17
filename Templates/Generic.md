---
dg-publish: true
tags: 
created: ""
---
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
>[!summary]- Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

# <%* tR += result %>

<% tp.file.cursor(1) %>

# Related
