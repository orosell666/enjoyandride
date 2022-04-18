import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import { Context } from "../store/appContext";
// falta useState para guardar la info del mail i passwprd
// funcion que se ejecute cuando haga onclick en el boton login=> hara un fetch a mi api (url del insomnia)




export const Login = () => {
    const { actions, store } = useContext(Context);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    let history = useHistory();
    function validateForm() {
        return email.length > 0 && password.length > 0;
    }


    function sideIn() { }
    return (
        <div className="container mt-5 ">
            <form className="justify-content-center">
                <div >
                    <input
                        autoFocus
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        placeholder="Email"
                    />
                </div>
                <div className="form-group">
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="Password"
                    />
                </div>

                <button
                    type="button"
                    className="btn btn-dark mt-3 "
                    //disabled={!validateForm()}
                    onClick={() => {
                        actions.generateToken(email, password)
                        store.respuesta.token ? history.push('/dashboard') : ""


                    }}
                >
                    Submit
                </button>




            </form>
        </div>
    );
};

