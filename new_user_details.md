Russian explanation of why we need such changes you can see here https://docs.google.com/document/d/1z1xyGixq2cfKc5W9Oyifu96NMFANsg9mGpXQVyeBtjg/edit#heading=h.tkgfsxl73kn0

```sql 
Table user_info{
  id int [pk, increment]
  user_id int [ref: - U.id]
  citizenship varchar [not null]
  religion religion [not null]
  birthdate varchar [not null]
  address varchar [note: 'Nullable']
  category_of_needy categories_of_needy [note: 'Nullable']
  }
```
```sql   
Enum categories_of_needy{
  large_families
  low_income_families
  retired_person
  single_parent_families
  orphan
  refuge
  person_without_a_fixed_residence_or_traveler_for_russians
  person_without_a_fixed_residence_or_traveler_for_foreign
  debtor
  people_who_have_devoted_themselves_to_islam_or_for_study_of_the_Quran
  children_or_adults_with_disabilities_or_people_with_severe_diseases
}
```
```sql 
Table adult{
  id int [pk, increment]
  passport_main_page base_64 [not null]
  passport_registration_page base_64 [not null]
  passport_children_page base_64 [not null]
  passport_marrige_page base_64 [not null]
  education varchar [note: 'Nullable']
  place_of_work varchar [note: 'Nullable']
  position_at_work varchar [note: 'Nullable']
  is_the_contact_person bool [note: 'Nullable']
  the_contact_person_phone varchar [note: 'Nullable']
  family_status family_status [note: 'Nullable']
  
  salary base_64  
  pension(retirement) base_64 [note: 'not null if its retired_person, in other cases nullable'] 
  allowance base_64 
  certificate_from_the_labor_exchange base_64
  
  employment_history_book base_64 [note: 'Nullable']
  divorce_certificate base_64 [note: 'not null if a person divorced']
  certificate_of_being_in_a_prison base_64 [note: 'not null if a person in prison']
 }
 ```
>desc. income statement for the last 6 months. At least one of them (salary, pension, allowance, certificate_from_the_labor_exchange) mustn't be null

```sql 
Table child{
  id int [pk, increment]
  parent1_id int [ref: < Parent.id]
  parent2_id int [ref: < Parent.id] [note: 'Nullable']
  birth_certificate base_64
  child_passport_main_page base_64
  child_registration_page base_64
  allowance base_64
}
```
>desc. A child start having a passport from 14 years, before that age they have only birth_certificate. So if child's age < 14 birth_certificate is not null and passport pages would be null. If child's age >= 14 birth_certificate could be null and passport pages would NOT be null.

Now let's see all types of needed documents for a request

1) if type=large_families or low_income_families
```sql 
   parent_1 adult [not null]
   parent_2 adult [not null]
   children child[] [not null]
   house_book base_64 [not null] 
   ```
    
>desc. The house book is a document containing information about tenants, employers, members of their families, is a kind of registration journal, which contains information about all citizens registered in residential premises of a private or multi-apartment residential building.

2) if type=retired_person
```sql 
  person adult [not null]
  family_composition_information varchar [note: 'Nullable but questionable, in this case we dont need to show all connections between marriage status and children info. Maybe just made a varchar field to keep info about that'] 
 ```
3) if type=single_parent_families
```sql 
  parent_1 adult [not null]
  parent_2 adult [note: 'not null if exists, for example, in prison']
  children child[] [not null]
  house_book base_64 [not null] 
  death_certificate_of_one_parent base_64 [note: 'questionable']
  ```
   
4) if type=orphan
```sql 
  orphan_guardian_1 adult [not null]
  orphan_guardian_2 adult [note: 'Nullable']
  child child [not null]
 ```

5) if type=refuge [note: 'questionable']
```sql 
  passport_of_homeland base_64 [not null]
  refugee_status_document base_64 [not null]
  ```

6) if type=person_without_a_fixed_residence_or_traveler(for russians)
```sql 
  person adult [not null]
  other_document base_64
  ```

7) if type=person_without_a_fixed_residence_or_traveler(for foreign)
```sql 
  passport_of_homeland base_64 [not null]
  other_document base_64
  ```

8) if type=debtor
```sql 
  person adult [not null]
  children child[] [note: 'Nullable']
  documents_confirming_debts base_64[] [not null]
  ```

9) if type=people_who_have_devoted_themselves_to_islam_or_for_study_of_the_Quran
  ```sql 
  person adult [not null]
  document_from_clergyman base_64
  document_from_education_place base_64
  certificate_from_the_labor_exchange base_64
  ```

10) if type=children_or_adults_with_disabilities_or_people_with_severe_diseases
```sql 
  parent_1 adult [not null]
  parent_2 adult [not null]
  child child [not null]
  disability_certificate base_64
  medical_certificate_from_the_doctor base_64 [not null]
  medical_bill base_64 [not null]
  ```


