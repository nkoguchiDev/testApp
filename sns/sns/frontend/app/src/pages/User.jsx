import styled from "styled-components";

import { EventCard } from "../components/Elements/EventCard";
import { MessageModal } from "../components/Elements/MessageModal";

const RightLowerMessageModal = styled.div`
    position: fixed;
    right: 0;
    bottom: 0;
    padding: 15px;
`;

export const User = () => {
    return (
        <>
            <EventCard />
            <RightLowerMessageModal>
                <MessageModal />
            </RightLowerMessageModal>
        </>
    );
};
