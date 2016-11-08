public static String[] getPos(String url) {

    //String[] qbs = {};

    JsonObjectRequest jsonObjReq = new JsonObjectRequest(Request.Method.GET,
            url, null, new Response.Listener<JSONObject>() {

        @Override
        public String[] onResponse(JSONObject response) {
            //Log.d("qbr", response.toString());

            try {
                //String balText = response.getString("bal");
                JSONArray testArr = response.getJSONArray("testArr");
                String[] qbs = new String[testArr.length()];
                for(int i=0;i<testArr.length();i++)
                {
                    JSONObject jb = (JSONObject) testArr.get(i);
                    String name = jb.getString("name");
                    String opp = jb.getString("opp");
                    String info = name +" -- "+ opp;
                    qbs[i] = info;
                    //Log.i("testArray",info);
                }
                return qbs;
                /*
                for(int i=0;i<qbs.length;i++)
                {
                    Log.i("qb", qbs[i]);
                }
                */

            }
            catch (JSONException e){
                e.printStackTrace();
                Log.i("testArray", "couldnt do it");
            }
        }

    }, new Response.ErrorListener() {

        @Override
        public void onErrorResponse(VolleyError error) {
            VolleyLog.d("qbr", "Error: " + error.getMessage());
        }
    });

    // Adding request to request queue
    AppController.getInstance().addToRequestQueue(jsonObjReq);
    //return qbs;
}

----

public String[] getQb() {

    InputStream inputStream = null;
    String result = "";

    //http request
    HttpClient httpclient = new DefaultHttpClient();

    // make GET request to the given URL
    HttpResponse httpResponse = httpclient.execute(new HttpGet("http://52.24.226.232/mgetQb"));

    // receive response as inputStream
    inputStream = httpResponse.getEntity().getContent();

    // convert inputstream to string
    if(inputStream != null)
        result = convertInputStreamToString(inputStream);
    else
        result = "Did not work!";
    //get response string

    //go string to jsonobject

    //turn json object to array with function
    JSONArray qbr = response.getJSONArray("qbr");
    String[] qbs = new String[qbr.length()];
    for(int i=0;i<qbr.length();i++)
    {
        JSONObject jb = (JSONObject) qbr.get(i);
        String name = jb.getString("name");
        String opp = jb.getString("opp");
        String info = name +" -- "+ opp;
        qbs[i] = info;
        //Log.i("testArray",info);
    }
    return qbs;
}

private static String convertInputStreamToString(InputStream inputStream) throws IOException{
    BufferedReader bufferedReader = new BufferedReader( new InputStreamReader(inputStream));
    String line = "";
    String result = "";
    while((line = bufferedReader.readLine()) != null)
        result += line;

    inputStream.close();
    return result;
}

---

public void getPos(String url) {

        JsonObjectRequest jsonObjReq = new JsonObjectRequest(Request.Method.GET,
                url, null, new Response.Listener<JSONObject>() {

            @Override
            public void onResponse(JSONObject response) {
                //Log.d("qbr", response.toString());

                try {
                    //String balText = response.getString("bal");
                    JSONArray qbr = response.getJSONArray("qbr");
                    String[] qbs = new String[qbr.length()];
                    for(int i=0;i<qbr.length();i++)
                    {
                        JSONObject jb = (JSONObject) qbr.get(i);
                        String name = jb.getString("name");
                        String opp = jb.getString("opp");
                        String info = name +" -- "+ opp;
                        qbs[i] = info;
                        //Log.i("testArray",info);
                    }
                /*
                for(int i=0;i<qbs.length;i++)
                {
                    Log.i("qb", qbs[i]);
                }
                */

                }
                catch (JSONException e){
                    e.printStackTrace();
                    Log.i("testArray", "couldnt do it");
                }
            }

        }, new Response.ErrorListener() {

            @Override
            public void onErrorResponse(VolleyError error) {
                VolleyLog.d("qbr", "Error: " + error.getMessage());
            }
        });

        // Adding request to request queue
        AppController.getInstance().addToRequestQueue(jsonObjReq);
    }

----

public static String[] getQb() {

        String[] qbshow = {"neil"};
        HttpClient Client = new DefaultHttpClient();

        try{
            String SetServerString = "";

            HttpGet httpget = new HttpGet("http://52.24.226.232/mgetQb");
            ResponseHandler<String> responseHandler = new BasicResponseHandler();
            SetServerString = Client.execute(httpget, responseHandler);

            Log.d("checkGet",SetServerString);
            JSONObject json = new JSONObject(SetServerString);

            //turn json object to array with function
            JSONArray qbr = json.getJSONArray("qbr");
            String[] qbs = new String[qbr.length()];
            for(int i=0;i<qbr.length();i++)
            {
                JSONObject jb = (JSONObject) qbr.get(i);
                String name = jb.getString("name");
                String opp = jb.getString("opp");
                String info = name +" -- "+ opp;
                qbs[i] = info;
                Log.i("qb",info);
            }
            return qbs;
            //qbshow = qbs;

        }
        catch(Exception e){
            Log.d("tag", e.toString());
        }
        //return qbs;
    }