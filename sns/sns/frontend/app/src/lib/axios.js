import Axios from "axios";

import { API_ENDPOINT } from "/app/src/config";

export const axios = Axios.create({
    baseURL: API_ENDPOINT,
    timeout: 1000,
});

axios.interceptors.response.use(
    (response) => {
        return response.data;
    },
    (error) => {
        return Promise.reject(error);
    }
);
