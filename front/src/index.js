import React from 'react';
import ReactDOM from 'react-dom';

// Service worker
import * as serviceWorker from './common/serviceWorker';

// App
import App from './App';
import { ApolloProvider } from 'react-apollo';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { ApolloClient } from 'apollo-client';
import { HttpLink } from 'apollo-link-http';


const cache = new InMemoryCache();


const client = new ApolloClient({
    cache: new InMemoryCache(),
    link: new HttpLink({
        uri: 'http://localhost:8000/gql',
        credentials: 'same-origin',
     }),
     cache
  // other options like cache
});


// 1

// 4
ReactDOM.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>,
  document.getElementById('root')
)
serviceWorker.unregister();


