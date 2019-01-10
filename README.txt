==================================================
--- Hypertext Labs Mission Statement + Roadmap ---
==================================================

=============
--- INDEX ---
=============

    1. Timeline Markers  
       
        a. Potential ==> POE
            a resource worth putting oversight into for potential return on functional efficency or other various benefactors 
        b. Framework ==> FWK
            foundation component in Hypertext's ecosystem - necessary for functional design system to run 
        c. Experimental ==> EXP
            these have surpassed potential markers and entered any stage of development or functional//system RnD
        d. Staging ==> STG
            this is where an integration or system has bypassed experimental and graduated to a more mature placement in the stacks ecosystem

=============
--- INDEX ---
=============


1. (STG) Graphql API wrapping - start w podio pkg for automated server architecture cinfiguratuion, then move to civic apis 

2. (FWK) Django Backend model infrastructure for Machine Learning Pipelines and serverless scalability 

3. (EXP) IPFS distributed + decentralized p2p storage methods (experimental)

4. (EXP) Nteract Based JupterNB/Lab tool - wrapped in  GQL and integrated with HypertextLabs + Civic Platform 

    (a) Build Materials 


        https://www.samlau.me/projects/2016-09-01-jupyterhub


    Electron for cross platform 
        
        https://electronjs.org/apps/graphiql
        https://github.com/nteract/nteract/issues/1346

    Electorn + Graphql 2 CIVIC APIS (mirrored CIVIC GQL APIS) - 

    (1) offline-first serverless distributed p2p database \ https://github.com/orbitdb/orbit-db
        
        Potential Proof of Work -
        a. Trimet - Transportation API - Realtime 
        b. Elections 
            *(include https://developers.google.com/civic-information/ and oregon voters pamphlet)
            https://sos.oregon.gov/elections/Documents/pamphlet/2018/general-book13.pdf
        

=============
--- Stack --- 
=============

Domain: hypertextlabs.co

(a) Stack

(FWK) Frontend: React, Apollo, Graphql 
(FWK) Backend: Django 
(STG) Database(s): Mysql, PostgreSQL v9.4 (FWK), Neo4J(EXP), AWS S3(STG)

(B) Workflow Tools

    (FWK) Version Control: Github

    (EXP) https://code.stdlib.com/ - stdlib API (FAAS)  
        
        (1) Backend (API) Snippets (existing integration; stripe, sms) buildout Podio Integration, + Metrc Testing + possibly partial(?) infrastructure
            
            Impact - rapid api iteration and deployment, first step to scale good way to organize component like, maintained microservices and api integrations

    (EXP) https://bitsrc.io/ - 
        
        (1) Bit Frontend (components) Bit helps you organize your components, share them as a team and keep them synced in all your projects. This environment enables you to use and develop components from other projects. For example, components written in typescript can be used and developed in a project written in flow-typed. It also lets Bit test and build your components in isolation, so you can know the exact state of every component.
            
            Impact - Reausable compnents to continually lower development overhead as we scale and onboard more work also maintains reusabiltiy and transparency between the design asoects and the apollo gql api integrations with third parties and our standalone apis 
            

=============================
--- Development Practices ---
=============================

This is an outline of development methodologies that ought to be taken up when building upon Hypertext Labs application architecture

    (a) Version Control: GitHub master/Launch/Production branches

    Component snippets - React/node API snippets vs Django/GQL/Python API snippets 
        
        *Focus on merge consistency between front and back of house  

    Snippets primarily live within Dev branch - 
    API snippets often move to Launch, Production will move to more permanent server architecture

    Workspace: VS Code, Python 3.5, React, autoDocs, DjangoSnippets *this is for consistency throughout the codebase

============================
--- Development Timeline ---
============================

    (a) Setup Workspace - git repo (local and on GitHub), create branches, instantiate React + Django + GQL stack

    (b) Configure Bit Component management

    (c) Configure code.stdlib cmd line tools + workspace for easy and efficient API prototyping and integration

==========================
--- django-pod package ---
==========================

Podio schema django package - this can later be generalized to generate based off common API docs, 
initially I figure it would be best to do it with swagger

Generate server architecture first... 

a. generate from pd workspace ==> django application
    1. cmd uses workspace_slug in django-admin startapp {workspace_slug}
    2. create schema.py file - import necessary for base 
    3. return list object of all the workspaces applications 

b. generate from pd app ==> django model 
    1. use application list object to take app_slug and generate schema type 
    2. for fields in app - return json object of app template 
    3. create mapping between podio field types and django model defs 
    4. use app template json object to generate unique django models with field_name and type 

c. field_handler def
    1. The key to this functionality is the field handler funciton 
        that handles the wiring between the podio app template json object*
    2. Note that we specifically focus on handling the podio object as a retruned 
        json object so we can extend this system fluidly to other platforms.


    =================
    --- User-Flow ---
    =================

    1. run django-admin startapp name -pd url_podio_workspace

        example: django-admin startapp distro -pd https://podio.com/applegate-solutions/budhubdistro

    - creates distro app
    - generates schema.py 

    - calls podio api to return two primary json object schemas
        1. list of included apps 
        2. for e app schema of fields 
    - podio 2 django schema converter generate the django models from field names and types 
    - shema.py is appended with mdoel Type defs and an objects_all query for each instantiated model 


==================
--- Interfaces ---
==================

(a) Initial React Homepage starter kit for home and about page for company - login, auth, admin pages in package

(b) Django Podio managment page
    1. enter workspace 
    2. recieve all apps
    3. select app or apps
    4. get fields for app or apps 
    5. create models and gql schema on backend 
    6. client will make necesarry query for items 
    7. 