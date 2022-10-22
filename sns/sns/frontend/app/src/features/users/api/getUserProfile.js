import { axios } from "/app/src/lib/axios";

export const getUserProfile = () => {
    return axios.get("/me", {
        withCredentials: true,
    });
};
