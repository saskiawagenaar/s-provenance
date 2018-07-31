# S-ProvFlow

Provenance framework for storage and access of data-intensive streaming lineage. It offers a a web API and a range of dedicated visualisation tools based on the underlying provenance model, S-PROV, which utilises and extends PROV and ProvONE models. S-PROV addresses aspects of mapping between logical representation and concrete implementation of a workflow until its enactment onto a target computational resource.  The model captures aspects associated with the distribution of the computation, runtime changes and support for flexible metadata management and discovery for the data products generated by the execution of a data-intensive workflow.

     
![alt tag](https://raw.githubusercontent.com/aspinuso/s-provenance/master/resources/s-prov-final.png)

- A collection of services including a WEB-API (provenance-api) and a front-end GUI (sprovflow-viewer) allowing acquisition and exploration of provenance data which is produced at a run-time by a computational engine. Below a schematic representation of the architecture and interaction with external resources, followed by screenshots of the interactive tools.

#### The API

 
S-ProvFlow system exposes a RESTful web API which offers high-level services on top of the storage backend. The API methods are classified in provenance acquisition, monitoring, data discovery and traceability, comprehensive-summaries, and provenance export. This is the service layer on top of which all the above visualisation and exploration tools are built. The API support the OpenAPI specs via the automatically generated [swagger 2.0](https://github.com/aspinuso/s-provenance/blob/master/provenance-api/resources/swagger.json) description.
 


The API returns information in JSON and JSON-LD, which includes PROV and S-PROV semantics and references to external controlled vocabularies for the domain metadata describng the data entities and the agents participating in their production. It allows clients to selectively export provenance traces in PROV-XML and RDF for a single data results, as well as for the entire computation.

![alt tag](https://raw.githubusercontent.com/KNMI/s-provenance/master/resources/sprovflowpnf.png)

#### Monitoring and Validation Visualiser (MVV)

The S-ProvFlow system offers a visual tool (Monitoring and Validation Visualiser- MVV) that allows different sorts of operations through the interactive access and manipulation of the provenance information. These include monitoring of the progress of the execution with runtime indication on the production of data and the occurrence of errors, dependency navigation, data discovery, data preview, download and selective staging.

![alt tag](https://raw.githubusercontent.com/KNMI/s-provenance/master/resources/totalv.png)

#### The Bulk Dependencies Visualiser (BDV)

The BVD produces comprehensive views for a single execution of a scientific data-intensive task or involving many runs and users. It exploits an approach to visual-analytics of the information captured that combines radial diagrams, selective grouping and Edge Bundles technique. Views of the provenance repository are generated interactively for multiple levels of granularity and for different kinds of expertise and roles. It offers facilities to tune and organise the views. 

![alt tag](https://raw.githubusercontent.com/KNMI/s-provenance/master/resources/bdv_combined_1_lscape1.png)
We consider two classes of usage, respectively addressing details of a single computational tasks (above) or the interaction between user and their methods (below), according to configurable metadata properties and values-ranges.

![alt tag](https://raw.githubusercontent.com/KNMI/s-provenance/master/resources/radial_duo.png)

#### Supporting Projects

- S-ProvFlow manages provenance traces provided by data-intesive systems such has dispel4py and its integration within the WPS (Web Processing Services), implemented with the PyWPS framework, is currently ongoing (https://github.com/KNMI/wps_workflow). 

- S-ProvFlow is the provenance framework integrated within the VERCE Earthquakes Simulation portal (http://portal.verce.eu) and the climate services portal (http://climate4impact.eu).

- S-ProvFlow is being further developed in the context of the H2020 project DARE http://project-dare.eu/


#### Dockerization

TODO: Discuss option to build locally and to pull from registry.

The s-prov project can be deployed using docker technology. The project is split into a store and viewer instances.  The viewer is currently set to connect via the docker bridge to a local instance of the store. Changes to the docker file are required if the viewer is remote.
The store instance is deployable via docker-compose, the mongo db instance is split from the store services api. The store service can also be deployed independently so as to be attached to an existing mongo db. 


s-prov store,
  see **provenance-api/docker-compose.yml**
```
  $ cd provenance-api
  $ docker-compose up --build 
```
s-prov viewer
```
   $ docker build sprovflow-viewer/ -t viewer 
   $ docker run -it -p9000:8080 viewer 
```   

Once the containers are up and running the following endpoints will be exposed:
- API: http://127.0.0.1:8082/swagger/
- Viewer: http://127.0.0.1:9000/sprovflow-viewer/html/view.jsp

#### Deployment on AWS
Currently the service is deployed on AWS.


## Requirements and dependencies

### provenance-explorer
- Compile, Maven2 >= v3.2.5
- Apache Tomcat >= v7.x
- Java proxy j2ep v1.0
 
### provenance-api
- gunicorn >= 19.7.1 (or any WSGI webserver)
- flask >= v0.12.1
- pymongo >= v3.4.0
- Mongodb >= v3.4.7

### Related Developments

- WPS-WORKFLOW: https://github.com/KNMI/wps_workflow
- dispel4py: https://github.com/dispel4py/dispel4py
- VERCE: https://github.com/KNMI/VERCE

