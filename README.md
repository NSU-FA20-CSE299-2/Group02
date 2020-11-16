![image](Documentation/Proposal/images/NSU.png)\
**Department of Electrical & Computer Engineering**

***North South University***

Farsad’s Store

Section 2\
Fall 2020

Supervised by\
Shaikh Shawon Arefin Shimon (SAS3)

**Team Members (Group 02)**

-----------------------------------------------------------------
| Name | ID | Email |
| ----- | ------| --------|
| Ilmiat Farhana | 1712428042 | ilmia.farhana@northsouth.edu |
| Sakib Sadman Shajib | 1731201042 | sakib.shajib173@northsouth.edu |
-----------------------------------------------------------------

Introduction
============

The proposed application will be selling products such as desktops,
laptops, computer accessories, SSDs, and other related technology
gadgets. Since, e-commerce is getting much popular as a new media to
expand and reach more customers, businesses are very eager to use such
technology.

The objective of this project is to develop a web site where products
can be viewed and users can buy items online using their PC or
smartphone.

This is a virtual store where customers can browse the catalog and add
products they want to buy to their cart. Later they can checkout the
items from their cart and choose to pay online or Payment on Delivery.

Description
===========

The general objective of the project is to design and develop an online
shopping experience. The system should have the following features:

-   A catalog of products with multiple categories.

-   User based cart management.

-   Online Payment or Payment on Delivery option.

-   Delivery Management System.

-   Inventory Management System.

-   Accounting Management System.

There will be three types of user:

-   Admin

-   Employee

-   Customer

Features
========

Catalog of Products
-------------------

Like shelves on a physical store, our online store will have products
which will be divided into different categories, the categories will be
dynamic, so employees can add new categories without accessing the code.

User Cart
---------

Every time an user adds a product to their cart, it’ll stay there till
the user checks it out or removes it.

Online Payment
--------------

There will be an online payment gateway for the users to pay using their
card or digital wallet, there will be a payment on delivery option as
well.

Delivery
--------

Users will be able to track their orders and see status of the delivery.

Inventory
---------

The system will automatically keep track of product availability
depending on the data provided by an employee.

Accounting
----------

The system will keep track of all the transactions of the system; such
as purchases, invoices, payments etc.

Technology
==========

We decided to use Django with REST API as our backend and React for our
Frontend.

Frontend
--------

Since our site needs to be attractive and smooth, we planned to use
React.JS, a javascript web framework, developed by Facebook. This will
give us plenty of wiggle room on how much customization we can make to
the system. The Frontend will generally deal with data viewing,
beautification of site, and send data back and from to the API.

Backend
-------

We are using Django, a python web framework as our backend system and
PostgreSQL as our Relational Database System. Django gives us a lot of
room to add functionality to our system. We will be building an API,
using the Django REST framework, which will bridge the connection
between backend and frontend.

Django will take care of authentication. We plan to use third part
authentication API to make sure people can login with their
Google/Facebook or other popular platform’s account.

### Payment method

We are planning to use SSLCommerz’s Sandbox as our payment gateway.

DevOps
======

The code will be configured with CI and CD using GitHub Actions. It’ll
automatically create pull requests when some basic tests are passed by
our code, and after we verify the pull requests to the main branch, the
CD will automatically deploy it to our cloud provider.

We will be using GCP/AWS/Azure as our Cloud provider. We will use their
Kubernetes solutions to automatically orchestrate our dockerized
application, so it runs and scales automatically on the fly.

Monetization
============

If the system is developed for one specific e-commerce company, then
it’d be used a tool. Since, an e-commerce company will be using this
tool to sell better their product, the system will have a significant
contribution to the revenue.

But if the system is developed as a platform where multiple e-commerce
sites shares the same codebase, then this system itself can be a product
and we can charge 5-7% sales margin to small business, or create a
monthly/yearly/perpetual licensing system, with addons like hosting,
customization, etc.

Social Impact
=============

During pandemics like the one we are currently experiencing right now
(COVID-19), some retail business had to sustain loss due to not having
safer ways to sell their product. Selling online was one of their key
strategies to overcome the issue. In order to sell online they needed to
develop e-commerce sites like the one we are developing. General purpose
solutions like WooCommerce, BigCommerce, Shopify, etc has very little
customizability and the stacks they were developed in are sometimes
close-source, backdated, or maybe even limited because of technology.
Our system would bring a change and make businesses run fully online and
make shopping experience better for customers.

Our system is helping people stay safe during a pandemic by shopping
online and it’s helping businesses keep running. Our system has the
ability to automatically scale, which eliminated system downtime. And
due to integration of tools like Inventory, Accounts, Payment, most of
the businesses’ employees can work from home.
