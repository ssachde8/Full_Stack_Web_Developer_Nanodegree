# P3 - Books Catalog

### Project Overview
> To Develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

### Why This Project?
> Modern web applications perform a variety of functions and provide amazing features and utilities to their users; but deep down, it’s really all just creating, reading, updating and deleting data. In this project, you’ll combine your knowledge of building dynamic websites with persistent data storage to create a web application that provides a compelling service to your users.

### What Will I Learn?
  * How to Develop a RESTful web application using the Python framework Flask
  * Implementing third-party OAuth authentication - Google, Facebook etc.
  * Implementing CRUD (create, read, update and delete) operations.
  * How to properly use the various HTTP methods available and how they relate to CRUD.
  * Properly implementing authentication mechanisms and appropriately mapping HTTP methods to CRUD operations are core features of a properly secured web application
  * Efficiently interacting with data is the backbone upon which performant web applications are built
  
### How to Run?

#### PreRequisites
  * [Python ~2.7](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)
  
#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Launch the Vagrant VM ( vagrant up )
  4. Find the catalog folder and replace it with the content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/ssachde8/Full_Stack_Web_Developer_Nanodegree/P3-Books-Catalog).

#### Launch Project
  1. Launch the Vagrant VM using command:
  
  ```
    $ vagrant up
  ```
  2. Run your application within the VM
  
  ```
    $ python /vagrant/catalog/application.py
  ```
  3. Access and test your application by visiting [http://localhost:7000](http://localhost:7000).
  
  ```
  Note: If the vagrant ssh command does not work for you, then follow these instructions:
    * https://github.com/Varying-Vagrant-Vagrants/VVV/wiki/Connect-to-Your-Vagrant-Virtual-Machine-with-PuTTY
  ```
