<h2 align="center">Project Report</h2>

<p align="center"><img src="Documentation/Proposal/images/NSU.png"></p>
<h2 align="center">Department of Electrical & Computer Engineering</h2>
<h1 align="center">North South University</h1>

<h3 align="center">Farsad’s Store </h3>

<p align="center">Section 2 <br>
Fall 2020</p>

<p align="center">Supervised by <br>
Shaikh Shawon Arefin Shimon (SAS3)</p>

<h2 align="center">Project Report</h2>

<h2 align="center">Team Members (Group 02)</h2>

<table align="center">
    <tr>
        <th>Name</th>
        <th>ID</th>
        <th>Email</th>
    </tr>
    <tr>
        <td>Ilmiat Farhana</td>
        <td>1712428042</td>
        <td>ilmia.farhana@northsouth.edu</td>
    </tr>
    <tr>
        <td>Sakib Sadman Shajib</td>
        <td>1731201042</td>
        <td>sakib.shajib173@northsouth.edu</td>
    </tr>
</table>


Introduction
===============

Project Idea:
The application will be selling products such as desktops, laptops, computer accessories, SSDs, and other related technology gadgets. Since, e-commerce is getting much popular as a new media to expand and reach more customers, businesses are very eager to use such technology. \par
The objective of this project is to develop a web site where products can be viewed and users can buy items online using their PC or smartphone. \par
This is a virtual store where customers can browse the catalog and add products they want to buy to their cart. Later they can check out the items from their cart and choose to pay online or Payment on Delivery.

Features: 
=========

* Users can see all their subject/course in the specific platform.
* Users can add or delete their subject/courses. To easy view which platform contains what subject
* Users will also be able to see posts of the specific subject/course sorted by subject and recent to old.

Technology
==========

Since our site needs to be attractive and smooth, we planned to use React.JS, a javascript web framework, developed by Facebook. This will give us plenty of wiggle room on how much customization we can make to the system. The Frontend will generally deal with data viewing, beautification of site, and send data back and from to the API.

Backend
-------
We are using Django, a python web framework as our backend system and PostgreSQL as our Relational Database System. Django gives us a lot of room to add functionality to our system. We will be building an API, using the Django REST framework, which will bridge the connection between backend and frontend. \par
Django will take care of authentication. We plan to use third part authentication API to make sure people can login with their Google/Facebook or other popular platform's account.

3.1 Proposed Technology Stack:
------------------------------

USER: Will keep info about the users signing in the application.
PLATFORM: The platform information for the signed in USER entity.
COURSE_INFO: The name of the course/subject associated with the specific platform

3.2 Implemented Technology Stack:
---------------------------------

Backend: Django, Django REST framework
Frontend: React

Businessplan/Monetization
=========================
If the system is developed for one specific e-commerce company, then it'd be used a tool. Since, an e-commerce company will be using this tool to sell better their product, the system will have a significant contribution to the revenue. 
But if the system is developed as a platform where multiple e-commerce sites shares the same codebase, then this system itself can be a product and we can charge 5-7\% sales margin to small business, or create a monthly/yearly/perpetual licensing system, with addons like hosting, customization, etc.

Conclusion
==========
During pandemics like the one we are currently experiencing right now (COVID-19), some retail business had to sustain loss due to not having safer ways to sell their product. Selling online was one of their key strategies to overcome the issue. In order to sell online they needed to develop e-commerce sites like the one we are developing. General purpose solutions like WooCommerce, BigCommerce, Shopify, etc has very little customizability and the stacks they were developed in are sometimes close-source, backdated, or maybe even limited because of technology. Our system would bring a change and make businesses run fully online and make shopping experience better for customers. 
Our system is helping people stay safe during a pandemic by shopping online and it's helping businesses keep running. Our system has the ability to automatically scale, which eliminated system downtime. And due to integration of tools like Inventory, Accounts, Payment, most of the businesses' employees can work from home.