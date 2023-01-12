class CreateMembers < ActiveRecord::Migration[7.0]
  def change
    create_table :members do |t|
      t.references :band, null: false, foreign_key: true
      t.string :name

      t.timestamps
    end
  end
end
