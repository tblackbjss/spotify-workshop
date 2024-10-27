# 1 Test API requests in Postman

In Postman, click on Workspaces → Create Workspace.

![Alt text](../assets/images/image.png)

Leave Blank workspace selected, click on Next.

![Alt text](../assets/images/image-1.png)

Call it Spotify API, leave Personal selected, click on Create.

![Alt text](../assets/images/image-2.png)

Click on Import.

![Alt text](../assets/images/image-3.png)

Click on files.

![Alt text](../assets/images/image-4.png)

Select "Spotify API.postman_collection.json" in the root folder of the project, click on Open.

![Alt text](../assets/images/image-5.png)

Click on Environments and then on the + icon to create a new one.

![Alt text](../assets/images/image-6.png)

Call it Spotify Tests.

![Alt text](../assets/images/image-7.png)

Go back to collections:

1. Select Spotify Tests as Environment
2. Set the Client ID and Secret in the Body of the request
3. Click on Send

![Alt text](../assets/images/image-8.png)

If the request was successful then you should get an access token back:

![Alt text](../assets/images/image-9.png)

And it should automatically be populated in the Spotify Tests environment:

![Alt text](../assets/images/image-10.png)

You can now explore the Spotify API using the documentation https://developer.spotify.com/documentation/web-api. Basic requests are included in the Postman collection.

![Alt text](../assets/images/image-11.png)