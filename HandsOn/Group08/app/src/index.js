import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { LoadScript } from "@react-google-maps/api";

import './index.css';
import routes from './routes';

const router = createBrowserRouter(routes)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <>
    <RouterProvider router={router} />
    <LoadScript googleMapsApiKey="API_KEY"/>
    </>
);
