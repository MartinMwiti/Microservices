import "./App.css";
import Main from "./main/Main";
import { BrowserRouter, Route } from "react-router-dom";
import Products from "./admin/Products";
import ProductCreate from "./admin/ProductsCreate";
import ProductEdit from "./admin/ProductEdit";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Route path="/" exact component={Main} />
        <Route path="/admin/products" exact component={Products} />
        <Route path="/admin/products/create" exact component={ProductCreate} />
        <Route path="/admin/products/:id/edit" exact component={ProductEdit} />
      </BrowserRouter>
    </div>
  );
}

export default App;
