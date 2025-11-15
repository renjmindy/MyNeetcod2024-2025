from typing import Dict, List
import uuid

class TicketManagementSystem:
    def __init__(self):
        self.tickets: Dict[str, Dict] = {}

    def sell_ticket(self, journey_id: str, price: float) -> str:
        trans_id = str(uuid.uuid4())
        self.tickets[trans_id] = {'journey_id': journey_id, 'price': price, 'is_group': False, 'group_trans_ids': []}
        return trans_id

    def refund_ticket(self, trans_id: str) -> bool:
        if trans_id in self.tickets:
            del self.tickets[trans_id]
            return True
        return False

    def get_transaction_info(self, trans_id: str) -> Dict | None:
        return self.tickets.get(trans_id)

    def sell_group_ticket(self, journey_id: str, num_tickets: int, price_per_ticket: float) -> List[str]:
        trans_ids = []
        for _ in range(num_tickets):
            trans_id = self.sell_ticket(journey_id, price_per_ticket)
            self.tickets[trans_id]['is_group'] = True
            trans_ids.append(trans_id)
        for trans_id in trans_ids:
            self.tickets[trans_id]['group_trans_ids'] = trans_ids
        return trans_ids

    def get_group_info(self, trans_id: str) -> List[Dict] | None:
        ticket_details = self.get_transaction_info(trans_id)
        if ticket_details and ticket_details['is_group']:
            return [self.get_transaction_info(group_trans_id) for group_trans_id in ticket_details['group_trans_ids']]
        return None

    def total_sales(self) -> float:
        return sum(ticket['price'] for ticket in self.tickets.values())

    def journey_sales_summary(self) -> Dict[str, int]:
        summary = {}
        for ticket in self.tickets.values():
            journey_id = ticket['journey_id']
            summary[journey_id] = summary.get(journey_id, 0) + 1
        return summary
        
    def merge_tickets(self, trans_ids: List[str]) -> str | None:
        total_price = 0
        reference_journey_id = self.tickets[trans_ids[0]]['journey_id']
        for tran_ids in trans_ids:
            if tran_ids in self.tickets:
                if self.tickets[tran_ids]['journey_id'] == reference_journey_id: total_price += self.tickets[tran_ids]['price']
                else: return None
            else: return None
                
        new_trans_id = self.sell_ticket(reference_journey_id, total_price)
        self.tickets[new_trans_id]['original_trans_ids'] = trans_ids
        
        for tran_ids in trans_ids:
            if tran_ids in self.tickets:
                if self.tickets[tran_ids]['journey_id'] == reference_journey_id: self.refund_ticket(tran_ids)
                else: return None
            else: return None
                
        self.tickets[new_trans_id]['is_merged'] = True
        
        return new_trans_id
        
    def split_ticket(self, trans_id: str, num_splits: int) -> List[str] | None:
        transList = list()
        if trans_id in self.tickets and num_splits >= 2:
            ticket_price = self.tickets[trans_id]['price']
            ticket_journeyID = self.tickets[trans_id]['journey_id']
            new_ticket_price = ticket_price / num_splits
            for _ in range(num_splits):
                transList.append(self.sell_ticket(ticket_journeyID, new_ticket_price))
            self.refund_ticket(trans_id)
        else: return None    
        
        return transList
        
            
