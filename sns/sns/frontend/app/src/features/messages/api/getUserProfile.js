import { axios } from "/app/src/lib/axios";

export const getMessageList = () => {
    return axios.get("/messages", {
        withCredentials: true,
    });
};
