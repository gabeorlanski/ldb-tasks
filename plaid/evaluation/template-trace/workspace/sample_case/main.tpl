Menu — {{title}}
{{! layout v2 }}
Tags: {{#tags}}[{{.}}]{{/tags}}
{{#items}}
  {{> item_row}}
{{/items}}
{{^drafts}}
No drafts pending.
{{/drafts}}
{{#zero}}
zero is truthy → {{.}}
{{/zero}}
Contact: {{owner.name}}
Motto: {{motto}} / {{{motto}}}
{{=<% %>=}}
<%#owner%>
Chez <%name%> — raw <%&name%>, braces {{stay}} literal
<%/owner%>
<%>footer%>
