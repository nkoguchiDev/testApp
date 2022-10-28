import styled from "styled-components";

import { HeaderOnLogin } from "../components/layouts/Header";
import { EventCard } from "../components/Elements/EventCard";
import { MessageModal } from "../components/Elements/MessageModal";

const _RightLowerMessageModal = styled.div`
    position: fixed;
    right: 0;
    bottom: 0;
    padding: 15px;
`;

export const UserHome = () => {
    return (
        <>
            <HeaderOnLogin user />
            <div>
                <ul id="userinfo"></ul>
            </div>
            <EventCard />
            <_RightLowerMessageModal>
                <MessageModal />
            </_RightLowerMessageModal>
        </>
    );
};
