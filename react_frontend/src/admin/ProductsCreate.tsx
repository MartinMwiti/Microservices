import React, { SyntheticEvent, useState } from "react";
import { Redirect } from "react-router";
import Wrapper from "./Wrapper";

const ProductCreate = () => {
  const [title, setTitle] = useState(""); // initial state = ""
  const [image, setImage] = useState(""); // initial state = ""
  const [redirect, setRedirect] = useState(false) // initial state = false
    

  // Call Backend
  const submit = async (e: SyntheticEvent) => {
    e.preventDefault();
    await fetch("http://localhost:8000/api/products", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title,
        image,
      }),
    });
    // If above call is successful, redirect to the products page
    setRedirect(true)
  };
  //   Redirect to products page
  if(redirect){
    return <Redirect to={'/admin/products'}/>
  }

  return (
    <Wrapper>
      <form onSubmit={submit}>
        <div className="form-group">
          <label>Title</label>
          <input
            type="text"
            className="form-control"
            name="title"
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Image</label>
          <input
            type="text"
            className="form-control"
            name="image"
            onChange={(e) => setImage(e.target.value)}
          />
        </div>
        <button className="btn btn-outline-secondary">Save</button>
      </form>
    </Wrapper>
  );
};

export default ProductCreate;
