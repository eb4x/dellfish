# Dummy Redfish API for Dell PowerEdge servers

The redfish api on actual hardware is orders of magnitute slower than just
spewing out static json blobs, which is what this project does. These json
blobs are grabbed from actual decommissioned systems.

This project was created to speed up the process of testing/developing zabbix
templates. And possibly verify expected behaviour.

The api expects an authorization header. The default username:password for Dell
iDRACs is root:calvin. Putting it all together you get;

`curl -H "Authorization: Basic cm9vdDpjYWx2aW4=" http://127.0.0.1:5000/redfish/v1/Systems`

## TODO
 * Simulate delays in the api (Zabbix has various timeouts for scripts)
 * Some way of enabling different PowerEdge models
 * More data from existing models/endpoints
 * Additional models
