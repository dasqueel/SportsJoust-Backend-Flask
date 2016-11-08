private void strObjReq(String url) {

    StringRequest myReq = new StringRequest(Method.POST,
                                            url,
                                            createMyReqSuccessListener(),
                                            createMyReqErrorListener()) {

        protected Map<String, String> getParams() throws com.android.volley.AuthFailureError {
            Map<String, String> params = new HashMap<String, String>();
            params.put("userName", "dasqueel");
            params.put("pwd", "1578");
            params.put("mtoken", "2i3bcib92fhe");
            return params;
        };
    };
    AppController.getInstance().addToRequestQueue(myReq);

}

/////////////////////

public class LoginRequest extends Request<String> {

    // ... other methods go here

    private Map<String, String> mParams;

    public LoginRequest(String param1, String param2, Listener<String> listener, ErrorListener errorListener) {
        super(Method.POST, "http://test.url", errorListener);
        mListener = listener;
        mParams = new HashMap<String, String>()
        mParams.put("paramOne", param1);
        mParams.put("paramTwo", param2);

    }

    @Override
    public Map<String, String> getParams() {
        return mParams;
    }
}
/////////////////

private void postOutcome(String url, JSONObject postJson, String contest, String mtoken, String outcome) {

    postJson.put("contest", contest);
    postJson.put("mtoken", mtoken);
    postJson.put("outcome", outcome);

    JsonObjectRequest jsonObjReq = new JsonObjectRequest(Method.POST,
            url, postJson, new Response.Listener<JSONObject>() {

        @Override
        public void onResponse(JSONObject response) {
            Log.d(TAG, response.toString());

            try {
                // Parsing json object response
                // response will be a json object
                String resp = response.getString("passed");

                if (resp.equals("rejection complete"))
                {
                    //do another postOutcome
                    displayMatch(postJson);

                } else if (passed.equals("matched")){
                    //make intest to wager activity
                    //pass match variables to wager activity
                } else if (passed.equals("matched")){
                    //first to accept, get another match
                    displayMatch(postJson);
                }

            } catch (JSONException e) {
                e.printStackTrace();
                Toast.makeText(getApplicationContext(),
                        "Error: " + e.getMessage(),
                        Toast.LENGTH_LONG).show();
            }
        }
    }, new Response.ErrorListener() {

        @Override
        public void onErrorResponse(VolleyError error) {
            VolleyLog.d(TAG, "Error: " + error.getMessage());
            Toast.makeText(getApplicationContext(),
                    error.getMessage(), Toast.LENGTH_SHORT).show();
        }
    });

    // Adding request to request queue
    AppController.getInstance().addToRequestQueue(jsonObjReq);
}

//////////////////////////////

public static void postWager(Context context,final String mtoken,final String wager,final String matchId){
    postWagerResponse.requestStarted();
    RequestQueue queue = Volley.newRequestQueue(context);
    StringRequest sr = new StringRequest(Request.Method.POST,"http://52.24.226.232/mpostWager", new Response.Listener<String>() {
        @Override
        public void onResponse(String response) {
            postWagerResponse.requestCompleted();
        }
    }, new Response.ErrorListener() {
        @Override
        public void onErrorResponse(VolleyError error) {
            postWagerResponse.requestEndedWithError(error);
        }
    }){
        @Override
        protected Map<String,String> getParams(){
            Map<String,String> params = new HashMap<String, String>();
            params.put("wager",wager);
            params.put("mtoken",mtoken);
            params.put("matchId", matchId);

            return params;
        }

        @Override
        public Map<String, String> getHeaders() throws AuthFailureError {
            Map<String,String> params = new HashMap<String, String>();
            params.put("Content-Type","application/x-www-form-urlencoded");
            return params;
        }
    };
    queue.add(sr);
}

public interface PostWagerResponseListener {
    public void requestStarted();
    public void requestCompleted();
    public void requestEndedWithError(VolleyError error);
}

///////////////////

/*
String matchUserStr = extras.getString("matchUser");
String matchOpStr = extras.getString("matchOp");
String uQbNameStr = extras.getString("uQbName");
String uRb1NameStr = extras.getString("uRb1Name");
String uRb2NameStr = extras.getString("uRb2Name");
String uWr1NameStr = extras.getString("uWr1Name");
String uWr2NameStr = extras.getString("uWr2Name");
String uTeNameStr = extras.getString("uTeName");
String uDefNameStr = extras.getString("uDefName");
String opQbNameStr = extras.getString("opQbName");
String opRb1NameStr = extras.getString("opRb1Name");
String opRb2NameStr = extras.getString("opRb2Name");
String opWr1NameStr = extras.getString("opWr1Name");
String opWr2NameStr = extras.getString("opWr2Name");
String opTeNameStr = extras.getString("opTeName");
String opDefNameStr = extras.getString("opDefName");
*/

/*
matchUser.setText(matchUserStr);
matchOp.setText(matchOpStr);
uQbName.setText(uQbNameStr);
uRb1Name.setText(uRb1NameStr);
uRb2Name.setText(uRb2NameStr);
uWr1Name.setText(uWr1NameStr);
uWr2Name.setText(uWr2NameStr);
uTeName.setText(uTeNameStr);
uDefName.setText(uDefNameStr);
opQbName.setText(opQbNameStr);
opRb1Name.setText(opRb1NameStr);
opRb2Name.setText(opRb2NameStr);
opWr1Name.setText(opWr1NameStr);
opWr2Name.setText(opWr2NameStr);
opTeName.setText(opTeNameStr);
opDefName.setText(opDefNameStr);
*/
///////////////////

private void postWager(String url, String mtoken, String matchId, int wage) {
    JSONObject postJson = new JSONObject();
    try {
        postJson.put("mtoken", mtoken);
        postJson.put("matchId", matchId);
        postJson.put("wage", wage);
    }
    catch (Exception e) {
        //
    }
    JsonObjectRequest jsonObjReq = new JsonObjectRequest(Request.Method.POST,
            url, postJson, new Response.Listener<JSONObject>() {

        @Override
        public void onResponse(String resp) {
            //Log.d("volleyResp", response.getString("outcome"));

            if (resp.equals("set new wager and turn"))
            {
                //go to matches main page
                Intent i = new Intent(getApplicationContext(), Home.class);
                startActivity(i);

            } else {
                //error handle -- nothing went through
                Log.i("wageVolley", "not working");
            }

        }
    }, new Response.ErrorListener() {

        @Override
        public void onErrorResponse(VolleyError error) {
            VolleyLog.d("volleyError", "Error: " + error.getMessage());
            Toast.makeText(getApplicationContext(),
                    error.getMessage(), Toast.LENGTH_SHORT).show();
        }
    });

    // Adding request to request queue
    AppController.getInstance().addToRequestQueue(jsonObjReq);
}