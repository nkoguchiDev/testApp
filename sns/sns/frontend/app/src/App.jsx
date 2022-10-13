import { BrowserRouter, Link, Switch, Route } from "react-router-dom";

import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { SignUp } from "./pages/SignUp";

export const App = () => {
    return (
        <BrowserRouter>
            <div className="Header">
                <Link to="/">Home</Link>
                <Link to="/Login">Login</Link>
                <Link to="/SignUp">SignUp</Link>

                <switch>
                    <Route exact path="/">
                        <Home />
                    </Route>
                </switch>
            </div>
        </BrowserRouter>
    );
};
