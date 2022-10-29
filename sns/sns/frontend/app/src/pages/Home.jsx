import * as React from "react";
import { useEffect } from "react";
import styled from "styled-components";

import { getUserProfile } from "../features/users/api/getUserProfile";
import { EventCard } from "../components/Elements/EventCard";
import { MessageModal } from "../components/Elements/MessageModal";

import { Header } from "../components/layouts/Header";

const RightLowerMessageModal = styled.div`
    position: fixed;
    right: 0;
    bottom: 0;
    padding: 15px;
`;
export const Home = () => {
    const [userAuth, setUserAuth] = React.useState(false);

    useEffect(() => {
        return () => {
            getUserProfile().then(
                (success) => {
                    setUserAuth(success);
                },
                (error) => {
                    setUserAuth(false);
                }
            );
        };
    }, []);

    if (userAuth) {
        return (
            <>
                <Header user={userAuth} />
                <EventCard />
                <RightLowerMessageModal>
                    <MessageModal />
                </RightLowerMessageModal>
            </>
        );
    } else {
        return (
            <div>
                <Header />
                <h1>Home</h1>
            </div>
        );
    }
};
