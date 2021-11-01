# devops-netology

Благодаря содержимому файла \devops-netology\terraform\.gitignore будут проигнорированы:

**/.terraform/* - всё содержимое каталога terraform

*.tfstate - файлы, имеющие расширение .tfstate
*.tfstate.* - файлы, имеющие в имени .tfstate.

crash.log - игнорировать файл crash.log

*.tfvars - все файлы с расширением .tfvars

override.tf - игнорировать все файлы override.tf
override.tf.json - игнорировать все файлы override.tf.json
*_override.tf - игнорировать все файлы, заканчивающиеся на _override.tf
*_override.tf.json - игнорировать все файлы, заканчивающиеся на _override.tf.json

.terraformrc - игнорировать файлы с расширением .terraformrc
terraform.rc - игнорировать файлы, заканчивающиеся на terraform.rc

# Новая строчка для задания 3
# Изменил файл для задания 4